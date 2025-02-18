import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_ZeroLagStochasticIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und ZeroLagStochasticIndicator
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'ZeroLagStochasticIndicator': {
                'class': ZeroLagStochasticIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagStochasticIndicator'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'ZeroLagStochasticIndicator': 1.0
        })
    )
