import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'SeasonalStrength': 1.0
        })
    )
