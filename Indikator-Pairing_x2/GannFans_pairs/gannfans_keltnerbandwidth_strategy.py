import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
