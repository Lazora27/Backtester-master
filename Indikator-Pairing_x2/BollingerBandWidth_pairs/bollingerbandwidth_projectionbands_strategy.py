import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'ProjectionBands': 1.0
        })
    )
