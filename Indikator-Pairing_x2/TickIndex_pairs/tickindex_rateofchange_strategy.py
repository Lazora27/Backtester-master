import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und RateOfChange
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'RateOfChange': 1.0
        })
    )
