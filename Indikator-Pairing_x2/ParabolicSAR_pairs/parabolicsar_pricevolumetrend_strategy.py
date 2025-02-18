import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
