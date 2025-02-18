import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und RateOfChange
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'RateOfChange': 1.0
        })
    )
