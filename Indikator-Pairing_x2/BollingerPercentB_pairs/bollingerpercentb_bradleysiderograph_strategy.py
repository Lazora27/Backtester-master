import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'BradleySiderograph': 1.0
        })
    )
