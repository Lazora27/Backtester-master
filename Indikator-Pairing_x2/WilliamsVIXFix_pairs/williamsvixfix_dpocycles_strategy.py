import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und DPOCycles
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'DPOCycles': 1.0
        })
    )
