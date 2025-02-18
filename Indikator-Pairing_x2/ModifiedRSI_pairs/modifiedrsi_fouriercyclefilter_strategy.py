import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
