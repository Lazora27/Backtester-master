import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
