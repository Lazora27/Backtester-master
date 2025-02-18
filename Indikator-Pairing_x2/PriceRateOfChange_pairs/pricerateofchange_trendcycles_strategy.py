import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und TrendCycles
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'TrendCycles': 1.0
        })
    )
