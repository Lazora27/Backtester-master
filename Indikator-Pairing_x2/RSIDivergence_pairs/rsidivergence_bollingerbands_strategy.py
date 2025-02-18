import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und BollingerBands
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'BollingerBands': 1.0
        })
    )
