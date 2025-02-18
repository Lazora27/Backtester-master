import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZeroLagStochasticIndicator_NormalizedVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZeroLagStochasticIndicator und NormalizedVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'ZeroLagStochasticIndicator': {
                'class': ZeroLagStochasticIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagStochasticIndicator'>
            },
            'NormalizedVolatilityIndex': {
                'class': NormalizedVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedVolatilityIndex'>
            }
        }),
        ('weights', {
            'ZeroLagStochasticIndicator': 1.0,
            'NormalizedVolatilityIndex': 1.0
        })
    )
