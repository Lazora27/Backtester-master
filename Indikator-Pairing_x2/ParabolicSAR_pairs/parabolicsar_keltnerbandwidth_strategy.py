import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
