import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und DPOCycles
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'DPOCycles': 1.0
        })
    )
