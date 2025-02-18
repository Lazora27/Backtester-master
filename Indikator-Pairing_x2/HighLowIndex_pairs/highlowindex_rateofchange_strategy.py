import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und RateOfChange
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'RateOfChange': 1.0
        })
    )
