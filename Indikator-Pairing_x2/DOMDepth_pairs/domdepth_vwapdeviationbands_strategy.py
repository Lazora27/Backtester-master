import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
