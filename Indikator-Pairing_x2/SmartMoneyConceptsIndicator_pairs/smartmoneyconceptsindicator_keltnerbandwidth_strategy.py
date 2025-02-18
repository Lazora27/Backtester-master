import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartMoneyConceptsIndicator_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartMoneyConceptsIndicator und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'SmartMoneyConceptsIndicator': {
                'class': SmartMoneyConceptsIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartMoneyConceptsIndicator'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'SmartMoneyConceptsIndicator': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
