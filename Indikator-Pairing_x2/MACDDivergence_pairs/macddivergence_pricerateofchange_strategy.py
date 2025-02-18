import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
