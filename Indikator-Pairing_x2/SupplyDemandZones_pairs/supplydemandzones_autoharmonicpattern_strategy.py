import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
