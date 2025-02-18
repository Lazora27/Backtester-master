import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'VortexIndicator': 1.0
        })
    )
