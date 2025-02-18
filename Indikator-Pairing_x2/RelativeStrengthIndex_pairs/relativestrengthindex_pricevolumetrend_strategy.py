import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
