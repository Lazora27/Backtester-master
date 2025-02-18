import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und OpenInterest
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'OpenInterest': 1.0
        })
    )
