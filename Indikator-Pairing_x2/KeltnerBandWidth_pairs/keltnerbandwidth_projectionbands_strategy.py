import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'ProjectionBands': 1.0
        })
    )
