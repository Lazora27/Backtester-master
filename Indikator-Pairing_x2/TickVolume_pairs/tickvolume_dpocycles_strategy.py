import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und DPOCycles
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'DPOCycles': 1.0
        })
    )
