import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und RateOfChange
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'RateOfChange': 1.0
        })
    )
