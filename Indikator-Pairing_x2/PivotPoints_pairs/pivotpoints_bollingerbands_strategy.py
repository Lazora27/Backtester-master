import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und BollingerBands
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'BollingerBands': 1.0
        })
    )
