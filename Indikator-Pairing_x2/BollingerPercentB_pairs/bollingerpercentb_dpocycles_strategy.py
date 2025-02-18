import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und DPOCycles
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'DPOCycles': 1.0
        })
    )
