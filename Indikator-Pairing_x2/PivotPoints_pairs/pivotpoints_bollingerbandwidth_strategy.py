import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
