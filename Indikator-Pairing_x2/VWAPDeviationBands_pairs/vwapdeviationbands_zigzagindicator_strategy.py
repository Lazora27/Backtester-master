import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
