import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'BollingerPercentB': 1.0
        })
    )
