import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'SeasonalStrength': 1.0
        })
    )
