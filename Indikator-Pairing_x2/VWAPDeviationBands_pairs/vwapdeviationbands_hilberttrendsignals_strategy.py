import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
