import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
