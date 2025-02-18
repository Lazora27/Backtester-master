import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
