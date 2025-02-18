import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'TRIXIndicator': 1.0
        })
    )
