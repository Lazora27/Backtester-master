import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
