import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_NVISignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und NVISignals
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'NVISignals': 1.0
        })
    )
