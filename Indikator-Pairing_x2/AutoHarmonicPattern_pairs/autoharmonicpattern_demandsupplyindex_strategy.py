import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
