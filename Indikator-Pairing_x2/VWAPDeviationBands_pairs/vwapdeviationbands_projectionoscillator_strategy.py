import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
