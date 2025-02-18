import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'ProjectionBands': 1.0
        })
    )
