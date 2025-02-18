import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_SmartMoneyConceptsIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und SmartMoneyConceptsIndicator
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'SmartMoneyConceptsIndicator': {
                'class': SmartMoneyConceptsIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartMoneyConceptsIndicator'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'SmartMoneyConceptsIndicator': 1.0
        })
    )
