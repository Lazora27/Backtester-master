import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'DPOCycles': 1.0
        })
    )
