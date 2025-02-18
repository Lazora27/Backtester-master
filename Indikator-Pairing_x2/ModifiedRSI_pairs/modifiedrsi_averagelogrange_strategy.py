import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'AverageLogRange': 1.0
        })
    )
