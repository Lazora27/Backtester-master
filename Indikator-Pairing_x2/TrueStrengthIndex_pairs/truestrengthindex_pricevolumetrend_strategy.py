import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
