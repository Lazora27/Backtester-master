import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
