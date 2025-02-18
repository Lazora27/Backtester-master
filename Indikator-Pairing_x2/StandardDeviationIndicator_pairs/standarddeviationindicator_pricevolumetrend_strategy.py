import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
