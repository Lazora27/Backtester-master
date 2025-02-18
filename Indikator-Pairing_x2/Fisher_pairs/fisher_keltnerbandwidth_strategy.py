import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
