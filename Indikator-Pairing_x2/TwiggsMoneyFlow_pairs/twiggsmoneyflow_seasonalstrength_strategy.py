import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwiggsMoneyFlow_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwiggsMoneyFlow und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'TwiggsMoneyFlow': {
                'class': TwiggsMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwiggsMoneyFlow'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'TwiggsMoneyFlow': 1.0,
            'SeasonalStrength': 1.0
        })
    )
