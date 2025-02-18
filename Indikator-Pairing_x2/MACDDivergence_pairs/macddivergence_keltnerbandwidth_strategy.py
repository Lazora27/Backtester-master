import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
