import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'ProjectionBands': 1.0
        })
    )
