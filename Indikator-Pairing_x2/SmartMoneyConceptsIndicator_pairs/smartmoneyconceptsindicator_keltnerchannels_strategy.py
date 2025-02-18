import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartMoneyConceptsIndicator_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartMoneyConceptsIndicator und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'SmartMoneyConceptsIndicator': {
                'class': SmartMoneyConceptsIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartMoneyConceptsIndicator'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'SmartMoneyConceptsIndicator': 1.0,
            'KeltnerChannels': 1.0
        })
    )
