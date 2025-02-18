import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
