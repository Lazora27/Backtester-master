import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_NVISignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und NVISignals
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'NVISignals': 1.0
        })
    )
